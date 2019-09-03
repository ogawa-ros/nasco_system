function Listerner (name, msg) {
    this.name = name;
    this.age = age;
    this.ros = new ROSLIB.Ros();

    var sub = new ROSLIB.Topic(
        {
        ros : this.ros,
        name : name,
        messageType : 'std_msgs/' + msg,
        }
    );

    sub.subscribe(function(message) {
        var res = message.data;
        <!--
        var el = document.createElement(name);
        el.innerHTML = res
        document.getElementById(name+'_value').appendChild(el);
        -->
    }
                 );

    return res
}
