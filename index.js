const io = require('socket.io-client');
const PythonShell =require('python-shell').PythonShell;

var socket = io('http://192.168.0.27:8080'); //send connection request to server

var engine,dis1,dis2;
var distance = {name:"distancefeed",frontOBJ:"",backOBJ:"",updateflag:'false'}

socket.on('connect',function () {
    
    console.log('current socket id : ',socket.id); //gives the socket(session) id once when connect event is triggered
    console.log('connected : ',socket.connected); //boolean result of if socket is connected
    socket.emit('to_Server','Robot connected');

    
    dis1 = new PythonShell('robot/dis1.py',{mode:'text'});
    
    dis1.on('message',(message)=>{ distance['frontOBJ']=message;distance['updateflag']='true';  });

    dis2  = new PythonShell('robot/dis2.py',{mode:'text'});
    dis2.on('message',(message)=>{ distance['backOBJ']=message;distance['updateflag']='true';  });
    
    


});

setInterval(function send_distance(){ 
    sendtoUSer(distance);
    distance['updateflag']='false';
}, 800);


socket.on('connect_timeout', (timeout) => {console.log('connection timed out\n -server did not respond');});

socket.on('disconnect', (reason) => { console.log('---disconnected---'); if (reason === 'io server disconnect'){ socket.connect(); }  });
    
    
socket.on('from_Server',(msg)=>                                 //Receive message from server----
{
    try 
    {
        eval(msg.name+'(msg)');                                //  Calling function with name as incoming msg object name
    } 
    catch (error) 
    {
        console.log('\nerror caught -\n',error.name,error.message,'\ncontinuing anyway...');
        
    }  
});    

 
function sendtoUSer(msg) {  socket.emit('from_Rpi',msg); }     //function to send  data to user


//objects to be sent

// var mesge = {name:"messge",message:"hello user",warning:"no warnings yet"};
 //setupdateflag to false if not updated
// var gps = {name:"gpsfeed",latitude:"311",longitude:"900",updateflag:'true'};


//------------------- functions to handle incoming objects and messages -------------------------------------------


function move(obj) 
{   
    var engine_arguments = [obj.name,obj.movespeed,obj.direction,obj.time]
    engine = new PythonShell('robot/engine.py',{mode:'text',args:engine_arguments});
    engine.on('message',(message)=>{
    console.log('engine python said : \n',message);  })
       
}
function turn(obj) 
{
    var engine_arguments = [obj.name,obj.sensitivity,obj.direction,obj.time]
    engine = new PythonShell('robot/engine.py',{mode:'text',args:engine_arguments});
    engine.on('message',(message)=>{
    console.log('engine python said : \n',message);})
}

function stop(obj) { engine.kill();  }

function messge(obj) {  console.log('message received from user -> \n ',obj); }




