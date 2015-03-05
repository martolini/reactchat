var Reflux = require('reflux');
var ChannelActions = require('../actions/ChannelActions');
var MessageActions = require('../actions/MessageActions');

var _channels = {};
var _currentID = null;

var ChannelStore = Reflux.createStore({
	listenables: ChannelActions,

	onInitialData: function(channels) {
		channels.forEach(function(channel) {
			if (_channels[channel.id]) {
				return;
			}
			_channels[channel.id] = channel;
			_currentID = channel.id;
		});
		this.sendTrigger();
	},

	getCurrentChannelID: function() {
		return _currentID;
	},

	getCurrentChannelName: function() {
		if (_channels[_currentID]) {
			return _channels[_currentID].name;
		}
		return null;
	},

	onMessagesLoaded: function() {
		this.sendTrigger();
	},

	onChannelSubmitted: function(channel) {
	},

	onChannelChanged: function(channelID) {
		_currentID = channelID;
		this.sendTrigger();
	},

	sendTrigger: function() {
		var orderedChannels = [];
		for (var id in _channels) {
			orderedChannels.push(_channels[id]);
		}
		this.trigger({
			currentChannelID: _currentID,
			channels: orderedChannels,
		});
	}

});

module.exports = ChannelStore;