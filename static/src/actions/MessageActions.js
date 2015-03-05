var Reflux = require('reflux');

var MessageActions = Reflux.createActions([
	"initialData",
	"submitMessage",
	"receivedMessage",
	"changeChannel",
]);

module.exports = MessageActions;