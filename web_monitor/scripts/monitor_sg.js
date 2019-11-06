var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});

/*-- 1st --*/

var 100ghz_1st_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_1st_freq",
    messageType : "std_msgs/Float64"
});
var 100ghz_1st_power = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_1st_power",
    messageType : "std_msgs/Float64"
});
var 100ghz_1st_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_1st_onoff",
    messageType : "std_msgs/Int32"
});

var 200ghz_1st_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_1st_freq",
    messageType : "std_msgs/Float64"
});
var 200ghz_1st_power = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_1st_power",
    messageType : "std_msgs/Float64"
});
var 200ghz_1st_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_1st_onoff",
    messageType : "std_msgs/Int32"
});

/*-- 2nd upper --*/

var 100ghz_2nd_upper_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_2nd_upper_freq",
    messageType : "std_msgs/Float64"
});
var 100ghz_2nd_upper_power = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_2nd_upper_power",
    messageType : "std_msgs/Float64"
});
var 100ghz_2nd_upper_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_2nd_upper_onoff",
    messageType : "std_msgs/Int32"
});

var 200ghz_2nd_upper_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_2nd_upper_freq",
    messageType : "std_msgs/Float64"
});
var 200ghz_2nd_upper_power = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_2nd_upper_power",
    messageType : "std_msgs/Float64"
});
var 200ghz_2nd_upper_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_2nd_upper_onoff",
    messageType : "std_msgs/Int32"
});

/*-- 2nd lower --*/

var 100ghz_2nd_lower_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_2nd_lower_freq",
    messageType : "std_msgs/Float64"
});
var 100ghz_2nd_lower_power = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_2nd_lower_power",
    messageType : "std_msgs/Float64"
});
var 100ghz_2nd_lower_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/100ghz_2nd_lower_onoff",
    messageType : "std_msgs/Int32"
});

var 200ghz_2nd_lower_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_2nd_lower_freq",
    messageType : "std_msgs/Float64"
});
var 200ghz_2nd_lower_power = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_2nd_lower_power",
    messageType : "std_msgs/Float64"
});
var 200ghz_2nd_lower_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/200ghz_2nd_lower_onoff",
    messageType : "std_msgs/Int32"
});


/*-- 100ghz --*/

100ghz_1st_freq.subscribe(function(message) {
    document.getElementById("100ghz_1st_freq").innerHTML = (message.data);
});

100ghz_1st_power.subscribe(function(message) {
    document.getElementById("100ghz_1st_power").innerHTML = (message.data);
});

100ghz_1st_onoff.subscribe(function(message) {
    document.getElementById("100ghz_1st_onoff").innerHTML = (message.data);
});

100ghz_2nd_upper_freq.subscribe(function(message) {
    document.getElementById("100ghz_2nd_upper_freq").innerHTML = (message.data);
});

100ghz_2nd_upper_power.subscribe(function(message) {
    document.getElementById("100ghz_2nd_upper_power").innerHTML = (message.data);
});

100ghz_2nd_upper_onoff.subscribe(function(message) {
    document.getElementById("100ghz_2nd_upper_onoff").innerHTML = (message.data);
});

100ghz_2nd_lower_freq.subscribe(function(message) {
    document.getElementById("100ghz_2nd_lower_freq").innerHTML = (message.data);
});

100ghz_2nd_lower_power.subscribe(function(message) {
    document.getElementById("100ghz_2nd_lower_power").innerHTML = (message.data);
});

100ghz_2nd_lower_onoff.subscribe(function(message) {
    document.getElementById("100ghz_2nd_lower_onoff").innerHTML = (message.data);
});

/*-- 200ghz --*/

200ghz_1st_freq.subscribe(function(message) {
    document.getElementById("200ghz_1st_freq").innerHTML = (message.data);
});

200ghz_1st_power.subscribe(function(message) {
    document.getElementById("200ghz_1st_power").innerHTML = (message.data);
});

200ghz_1st_onoff.subscribe(function(message) {
    document.getElementById("200ghz_1st_onoff").innerHTML = (message.data);
});

200ghz_2nd_upper_freq.subscribe(function(message) {
    document.getElementById("200ghz_2nd_upper_freq").innerHTML = (message.data);
});

200ghz_2nd_upper_power.subscribe(function(message) {
    document.getElementById("200ghz_2nd_upper_power").innerHTML = (message.data);
});

200ghz_2nd_upper_onoff.subscribe(function(message) {
    document.getElementById("200ghz_2nd_upper_onoff").innerHTML = (message.data);
});

200ghz_2nd_lower_freq.subscribe(function(message) {
    document.getElementById("200ghz_2nd_lower_freq").innerHTML = (message.data);
});

200ghz_2nd_lower_power.subscribe(function(message) {
    document.getElementById("200ghz_2nd_lower_power").innerHTML = (message.data);
});

200ghz_2nd_lower_onoff.subscribe(function(message) {
    document.getElementById("200ghz_2nd_lower_onoff").innerHTML = (message.data);
});
