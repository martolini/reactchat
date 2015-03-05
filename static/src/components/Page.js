var React = require('react');
var MessageList = require('./MessageList');
var MessageComposer = require('./MessageComposer');
var Page = React.createClass({

	render: function() {
		return (
			<div id="page-content-wrapper">
				<div className='message-section'>
					<MessageList />
					<MessageComposer />
				</div>
			</div>
		);
	}

});

module.exports = Page;