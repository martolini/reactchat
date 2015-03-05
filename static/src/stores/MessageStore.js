var Reflux = require('reflux');
var MessageActions = require('../actions/MessageActions');
var ChannelActions = require('../actions/ChannelActions');
var ChannelStore = require('./ChannelStore');

var _messages = {};

function _getMessagesForChannel(channelID) {
	var messages = [];
	for (var id in _messages) {
		if (_messages[id].channelID == channelID) {
			messages.push(_messages[id]);
		}
	}
	return messages;
}

var MessageStore = Reflux.createStore({
	listenables: [MessageActions],

	init: function() {
		this.listenTo(ChannelStore, this.onChannelStoreChanged);
		this.channelID = ChannelStore.getCurrentChannelID();
	},

	onChannelStoreChanged: function(data) {
		this.trigger(_getMessagesForChannel(data.currentChannelID));
	},

	onInitialData: function(messages, channels) {
		messages.forEach(function(message) {
			if (!_messages[message.id]) {
				_messages[message.id] = {
					id: message.id,
					author: message.username,
					channelID: message.channel_id,
					text: message.text,
					created_at: new Date(message.created_at)
				}
			}
		});
		ChannelActions.initialData(channels);
	},

	onSubmitMessage: function(text, channelID) {
		message = {
			text: text,
			channelID: channelID
		}
		window.conn.send(JSON.stringify(message));
	},

	onReceivedMessage: function(message) {
		_messages[message.id] = {
			id: message.id,
			author: message.username,
			channelID: message.channel_id,
			text: message.text,
			created_at: new Date(message.created_at)
		}
		this.trigger(_getMessagesForChannel(ChannelStore.getCurrentChannelID()));
	},

	onChannelChanged: function(channelID) {
		this.trigger(_getMessagesForChannel(channelID));
	},


});

module.exports = MessageStore;