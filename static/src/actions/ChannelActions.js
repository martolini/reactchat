var Reflux = require('reflux');

var ChannelActions = Reflux.createActions([
	"initialData",
	"messagesLoaded",
	"channelReceived",
	"channelSubmitted",
	"channelChanged",
]);

module.exports = ChannelActions;