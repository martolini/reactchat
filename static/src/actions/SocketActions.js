var Reflux = require('reflux');

var SocketActions = Reflux.createActions(["socketConnect", "socketDisconnect"]);

module.exports = SocketActions;