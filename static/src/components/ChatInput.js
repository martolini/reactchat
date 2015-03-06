var React = require('react');

var ChatInput = React.createClass({

  getInitialState: function() {
    return {
      author: '',
      text: '',
    };
  },

  _onChangeAuthor: function(e) {
    this.setState({author: e.target.value});
  },

  _onChangeText: function(e) {
    this.setState({text: e.target.value});
  },

  _onKeyDown: function(e) {
    if (e.keyCode == 13) {
      this.props.addMessage(this.state)
      this.setState({text: ''});
    }
  },

  render: function() {
    return (
      <div>
        <form className='form form-inline'>
          <input className='form-control' ref='author' type='text' placeholder="Name" value={this.state.author} onChange={this._onChangeAuthor} />
          <input className='form-control' ref="text" type='text' placeholder="Your message" value={this.state.text} onChange={this._onChangeText} onKeyDown={this._onKeyDown} />
        </form>
      </div>
    );
  }
});

module.exports = ChatInput;