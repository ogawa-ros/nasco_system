function Listerner (name, msg) {
    this.name = name;
    this.age = age;
    this.ros = new ROSLIB.Ros();

    var sub = new ROSLIB.Topic(
        {
            ros : this.ros,
            name : this.name,
            messageType : 'std_msgs/' + this.msg,
        }
    );

    sub.subscribe(function(message) {
        var res = message.data;
    }
                 )

    return res
}
