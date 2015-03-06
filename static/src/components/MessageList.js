var React = require('react');
var Reflux = require('reflux');
var MessageStore = require('../stores/MessageStore');
var ChannelStore = require('../stores/ChannelStore');
var MessageComposer = require('./MessageComposer');

var MessageList = React.createClass({
	mixins: [Reflux.connect(MessageStore, "messages")],

	getInitialState: function() {
		return {
			messages: [],
		};
	},

	componentDidUpdate: function() {
		var node = this.getDOMNode();
		node.scrollTop = node.scrollHeight;
	},

	render: function() {
		var messages = this.state.messages.map(function(message, index) {
			var text = message.text.split("\n").map(function(subtext, i) {
				return (
					<p key={i} className="message-text">{ subtext }</p>
				);
			});
			return (
				<li className="message-list-item" key={message.id} >
					<div className='message-img pull-left'>
						<img src="http://placehold.it/50/55C1E7" alt="User Avatar" className="img-circle" />
					</div>
					<div className="message-header">
						<strong>{message.author}</strong>
						<small className="message-time text-muted"><i className="fa fa-fw fa-clock-o"></i>{ message.created_at.toLocaleTimeString() }</small>
					</div>
					<div className="message-body">
						{ text }
					</div>
				</li>
			);
		});

		return (
			<ul className='message-list'>
				{ messages }
			</ul>
		);
	}

});

module.exports = MessageList;