var React = require('react');
var ChannelList = require('./ChannelList');

var Sidebar = React.createClass({

	render: function() {
		return (
			<div id="sidebar-wrapper">
				<ul className="sidebar-nav">
					<li className="sidebar-brand">
						<a>sharexio</a>
					</li>
				<ChannelList />
				</ul>
			</div>
		);
	}

});

module.exports = Sidebar;