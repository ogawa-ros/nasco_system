var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});

/*-- 1st --*/

var sg_100ghz_1st_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_1st_freq_web",
    messageType : "std_msgs/Float64"
});
var sg_100ghz_1st_power = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_1st_power_web",
    messageType : "std_msgs/Float64"
});
var sg_100ghz_1st_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_1st_onoff_web",
    messageType : "std_msgs/String"
});

var sg_200ghz_1st_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_1st_freq_web",
    messageType : "std_msgs/Float64"
});
var sg_200ghz_1st_power = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_1st_power_web",
    messageType : "std_msgs/Float64"
});
var sg_200ghz_1st_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_1st_onoff_web",
    messageType : "std_msgs/String"
});

/*-- 2nd upper --*/

var sg_100ghz_2nd_upper_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_2nd_upper_freq_web",
    messageType : "std_msgs/Float64"
});
var sg_100ghz_2nd_upper_power = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_2nd_upper_power_web",
    messageType : "std_msgs/Float64"
});
var sg_100ghz_2nd_upper_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_2nd_upper_onoff_web",
    messageType : "std_msgs/String"
});

var sg_200ghz_2nd_upper_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_2nd_upper_freq_web",
    messageType : "std_msgs/Float64"
});
var sg_200ghz_2nd_upper_power = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_2nd_upper_power_web",
    messageType : "std_msgs/Float64"
});
var sg_200ghz_2nd_upper_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_2nd_upper_onoff_web",
    messageType : "std_msgs/String"
});

/*-- 2nd lower --*/

var sg_100ghz_2nd_lower_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_2nd_lower_freq_web",
    messageType : "std_msgs/Float64"
});
var sg_100ghz_2nd_lower_power = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_2nd_lower_power_web",
    messageType : "std_msgs/Float64"
});
var sg_100ghz_2nd_lower_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_100ghz_2nd_lower_onoff_web",
    messageType : "std_msgs/String"
});

var sg_200ghz_2nd_lower_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_2nd_lower_freq_web",
    messageType : "std_msgs/Float64"
});
var sg_200ghz_2nd_lower_power = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_2nd_lower_power_web",
    messageType : "std_msgs/Float64"
});
var sg_200ghz_2nd_lower_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/sg_200ghz_2nd_lower_onoff_web",
    messageType : "std_msgs/String"
});


/*-- 100ghz --*/

sg_100ghz_1st_freq.subscribe(function(message) {
    document.getElementById("sg_100ghz_1st_freq").innerHTML = (message.data);
});

sg_100ghz_1st_power.subscribe(function(message) {
    document.getElementById("sg_100ghz_1st_power").innerHTML = (message.data);
});

sg_100ghz_1st_onoff.subscribe(function(message) {
    document.getElementById("sg_100ghz_1st_onoff").innerHTML = (message.data);
});

sg_100ghz_2nd_upper_freq.subscribe(function(message) {
    document.getElementById("sg_100ghz_2nd_upper_freq").innerHTML = (message.data);
});

sg_100ghz_2nd_upper_power.subscribe(function(message) {
    document.getElementById("sg_100ghz_2nd_upper_power").innerHTML = (message.data);
});

sg_100ghz_2nd_upper_onoff.subscribe(function(message) {
    document.getElementById("sg_100ghz_2nd_upper_onoff").innerHTML = (message.data);
});

sg_100ghz_2nd_lower_freq.subscribe(function(message) {
    document.getElementById("sg_100ghz_2nd_lower_freq").innerHTML = (message.data);
});

sg_100ghz_2nd_lower_power.subscribe(function(message) {
    document.getElementById("sg_100ghz_2nd_lower_power").innerHTML = (message.data);
});

sg_100ghz_2nd_lower_onoff.subscribe(function(message) {
    document.getElementById("sg_100ghz_2nd_lower_onoff").innerHTML = (message.data);
});

/*-- 200ghz --*/

sg_200ghz_1st_freq.subscribe(function(message) {
    document.getElementById("sg_200ghz_1st_freq").innerHTML = (message.data);
});

sg_200ghz_1st_power.subscribe(function(message) {
    document.getElementById("sg_200ghz_1st_power").innerHTML = (message.data);
});

sg_200ghz_1st_onoff.subscribe(function(message) {
    document.getElementById("sg_200ghz_1st_onoff").innerHTML = (message.data);
});

sg_200ghz_2nd_upper_freq.subscribe(function(message) {
    document.getElementById("sg_200ghz_2nd_upper_freq").innerHTML = (message.data);
});

sg_200ghz_2nd_upper_power.subscribe(function(message) {
    document.getElementById("sg_200ghz_2nd_upper_power").innerHTML = (message.data);
});

sg_200ghz_2nd_upper_onoff.subscribe(function(message) {
    document.getElementById("sg_200ghz_2nd_upper_onoff").innerHTML = (message.data);
});

sg_200ghz_2nd_lower_freq.subscribe(function(message) {
    document.getElementById("sg_200ghz_2nd_lower_freq").innerHTML = (message.data);
});

sg_200ghz_2nd_lower_power.subscribe(function(message) {
    document.getElementById("sg_200ghz_2nd_lower_power").innerHTML = (message.data);
});

sg_200ghz_2nd_lower_onoff.subscribe(function(message) {
    document.getElementById("sg_200ghz_2nd_lower_onoff").innerHTML = (message.data);
});
