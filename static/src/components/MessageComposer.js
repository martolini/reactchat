var React = require('react');
var MessageActions = require('../actions/MessageActions');
var ChannelStore = require('../stores/ChannelStore');

var ENTER_KEY_CODE = 13;

var MessageComposer = React.createClass({

	getInitialState: function() {
		return {
			text: '' 
		};
	},

	_onChange: function(event, value) {
		this.setState({text: event.target.value});
	},

	_onKeyDown: function(event) {
		if (event.keyCode == ENTER_KEY_CODE && !(event.shiftKey)) {
			event.preventDefault();
			var text = this.state.text.trim();
			if (text) {
				MessageActions.submitMessage(text, ChannelStore.getCurrentChannelID());
			}
			this.setState({text: ''});
		}
	},

	render: function() {
		return (
			<div className='message-composer'>
				<textarea
					className="message-input form-control"
					name="message"
					autoCorrect="off"
					spellCheck="true"
					rows="1"
					value={this.state.text}
					onChange={this._onChange}
					onKeyDown={this._onKeyDown}
				/>
			</div>
		);
	}

});

module.exports = MessageComposer;