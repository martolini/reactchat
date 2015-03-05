var Reflux = require('reflux');
var SocketActions = require('../actions/SocketActions');

var StatusStore = Reflux.createStore({
	listenables: SocketActions,

	onSocketConnect: function() {
		this.trigger(true);
	},

	onSocketDisconnect: function(data) {
		this.trigger(false);
	}
});

module.exports = StatusStore;