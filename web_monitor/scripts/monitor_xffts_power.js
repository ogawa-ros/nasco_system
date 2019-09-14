var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});


var xffts_power_board01 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board01",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board02 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board02",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board03 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board03",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board04 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board04",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board05 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board05",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board06 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board06",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board07 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board07",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board08 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board08",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board09 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board09",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board10 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board10",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board11 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board11",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board12 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board12",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board13 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board13",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board14 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board14",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board15 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board15",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});

var xffts_power_board16 = new ROSLIB.Topic({
    ros : ros,
    name : "/xffts_power_board16",
    messageType : "nascorx_xffts/XFFTS_totalp_msg"
});


xffts_power_board01.subscribe(function(message) {
    document.getElementById("xffts_power_board01").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);
    });

xffts_power_board02.subscribe(function(message) {
    document.getElementById("xffts_power_board02").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board03.subscribe(function(message) {
    document.getElementById("xffts_power_board03").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board04.subscribe(function(message) {
    document.getElementById("xffts_power_board04").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board05.subscribe(function(message) {
    document.getElementById("xffts_power_board05").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board06.subscribe(function(message) {
    document.getElementById("xffts_power_board06").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board07.subscribe(function(message) {
    document.getElementById("xffts_power_board07").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board08.subscribe(function(message) {
    document.getElementById("xffts_power_board08").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board09.subscribe(function(message) {
    document.getElementById("xffts_power_board09").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board10.subscribe(function(message) {
    document.getElementById("xffts_power_board10").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
});

xffts_power_board11.subscribe(function(message) {
    document.getElementById("xffts_power_board11").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
})

xffts_power_board12.subscribe(function(message) {
    document.getElementById("xffts_power_board12").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
})

xffts_power_board13.subscribe(function(message) {
    document.getElementById("xffts_power_board13").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
})

xffts_power_board14.subscribe(function(message) {
    document.getElementById("xffts_power_board14").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
})

xffts_power_board15.subscribe(function(message) {
    document.getElementById("xffts_power_board15").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
})

xffts_power_board16.subscribe(function(message) {
    document.getElementById("xffts_power_board16").innerHTML = Math.log10(message.total_power).toFixed(3);
    sleep(1000);    
})
