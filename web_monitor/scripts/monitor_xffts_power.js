var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});


var xffts_power_board01 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board01_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board02 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board02_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board03 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board03_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board04 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board04_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board05 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board05_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board06 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board06_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board07 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board07_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board08 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board08_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board09 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board09_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board10 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board10_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board11 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board11_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board12 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board12_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board13 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board13_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board14 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board14_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board15 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board15_web",
    messageType : "std_msgs/Float64"
});

var xffts_power_board16 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board16_web",
    messageType : "std_msgs/Float64"
});


xffts_power_board01.subscribe(function(message) {
    document.getElementById("xffts_power_board01").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);
    });

xffts_power_board02.subscribe(function(message) {
    document.getElementById("xffts_power_board02").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);
});

xffts_power_board03.subscribe(function(message) {
    document.getElementById("xffts_power_board03").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
});

xffts_power_board04.subscribe(function(message) {
    document.getElementById("xffts_power_board04").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
});

xffts_power_board05.subscribe(function(message) {
    document.getElementById("xffts_power_board05").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
});

xffts_power_board06.subscribe(function(message) {
    document.getElementById("xffts_power_board06").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
});

xffts_power_board07.subscribe(function(message) {
    document.getElementById("xffts_power_board07").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
});

xffts_power_board08.subscribe(function(message) {
    document.getElementById("xffts_power_board08").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
});

xffts_power_board09.subscribe(function(message) {
    document.getElementById("xffts_power_board09").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
});

xffts_power_board10.subscribe(function(message) {
    document.getElementById("xffts_power_board10").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
});

xffts_power_board11.subscribe(function(message) {
    document.getElementById("xffts_power_board11").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
})

xffts_power_board12.subscribe(function(message) {
    document.getElementById("xffts_power_board12").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
})

xffts_power_board13.subscribe(function(message) {
    document.getElementById("xffts_power_board13").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
})

xffts_power_board14.subscribe(function(message) {
    document.getElementById("xffts_power_board14").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
})

xffts_power_board15.subscribe(function(message) {
    document.getElementById("xffts_power_board15").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
})

xffts_power_board16.subscribe(function(message) {
    document.getElementById("xffts_power_board16").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(3000);    
})
