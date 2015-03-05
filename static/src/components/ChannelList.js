var React = require('react');
var Reflux = require('reflux');
var ChannelStore = require('../stores/ChannelStore');
var ChannelActions = require('../actions/ChannelActions');

var ChannelList = React.createClass({
	mixins: [Reflux.listenTo(ChannelStore, 'onChannelStoreChange')],

	getInitialState: function() {
		return {
			currentChannelID: -1,
			channels: [] 
		};
	},

	onChannelStoreChange: function(data) {
		this.setState(data);
	},

	onCurrentChannelChange: function(channelID) {
		if (channelID != this.state.currentChannelID) {
			ChannelActions.channelChanged(channelID);
		}
	},

	render: function() {
		var channels = this.state.channels.map(function(channel, index) {
			var className = 'channel';
			if (channel.id == this.state.currentChannelID) {
				className += ' active';
			}
			return (
				<li className={className} onClick={ this.onCurrentChannelChange.bind(this, channel.id) } key={channel.id}>
					<a>#{channel.name}</a>
				</li>
			);
		}, this);
		return (
			<ul className="channel-list">
				<li>
					<h3>channels</h3>
				</li>
				{ channels }
			</ul>
		);
	}

});

module.exports = ChannelList;