var React = require('react');
var Reflux = require('reflux');
var StatusStore = require('./stores/StatusStore');
var SocketActions = require('./actions/SocketActions');
var MessageActions = require('./actions/MessageActions');
var ChannelActions = require('./actions/ChannelActions');
var Sidebar = require('./components/Sidebar');
var Page = require('./components/Page');

var socketRouter = function() {
	window.conn = new SockJS(window.url);
	conn.onopen = function() { SocketActions.socketConnect(); }
	conn.onclose = function() { SocketActions.socketDisconnect(); }
	conn.onmessage = function(data) {
		switch (data.data.type) {
			case 'message':
				MessageActions.receivedMessage(JSON.parse(data.data.message));
				break;
			case 'initial_data':
				MessageActions.initialData(JSON.parse(data.data.messages), JSON.parse(data.data.channels));
				break;
			default:
				break;
		}
	}

};
socketRouter();

var App = React.createClass({
	mixins: [Reflux.listenTo(StatusStore, "onStatusChange")],

	onStatusChange: function(status) {
		this.setState({
			status: status
		});
	},

	getInitialState: function() {
		return {
			status: false 
		};
	},

	render: function() {

		if (!this.state.status) {
			return (
				<div className="container-fluid">
					<p>Disconnected</p>
				</div>
			)
		}
		else {
			return (
				<div id="wrapper">
					<Sidebar />
					<Page />
				</div>
			)
		}
	}
});

React.render(
  <App />, document.getElementById('app')
);