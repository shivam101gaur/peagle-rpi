const io = require('socket.io-client');
const PythonShell =require('python-shell').PythonShell;
const path = require('path');


//-------!----------<< Enter the static SERVER ADDRESS below !!  >>---------!-------//


var socket = io('http://192.168.0.27:8080');


//-------!----------<< Enter the static SERVER ADDRESS above !!  >>---------!-------//


var engine,dis1,dis2,gps;
var distance = {name:"distancefeed",frontOBJ:"",backOBJ:"",updateflag:'false'};
var gpsfeed = {name:"gpsfeed",latitude:"",longitude:""};

  //send connection request to server

socket.on('connect',function () {
    
    console.log('current socket id : ',socket.id); //gives the socket(session) id once when connect event is triggered
    console.log('connected : ',socket.connected); //boolean result of if socket is connected
    socket.emit('to_Server','Robot connected');

    
    dis1 = new PythonShell(__dirname+'/robot/dis1.py',{mode:'text'});
    
    dis1.on('message',(message)=>{ distance['frontOBJ']=message;distance['updateflag']='true';  });

    dis2  = new PythonShell(__dirname+'/robot/dis2.py',{mode:'text'});
    dis2.on('message',(message)=>{ distance['backOBJ']=message;distance['updateflag']='true';  });
    
    gps = new PythonShell(__dirname+'/robot/gps.py',{mode:'text'});
    gps.on('message',(message)=>
    {
       
        console.log(message,typeof message);
        var arr = message.split(" , ");
        var lat = Number(arr[0]);
        var longi = Number(arr[1]);
        gpsfeed['latitude']=lat;
        gpsfeed['longitude']=longi;
        sendtoUSer(gpsfeed);
        
        
        
    });
    gps.on('close',()=>{
        console.log('terminated');
        
        
        
    });


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




//------------------- functions to handle incoming objects and messages -------------------------------------------


function move(obj) 
{   
    var engine_arguments = [obj.name,obj.movespeed,obj.direction,obj.time]
    engine = new PythonShell(__dirname+'/robot/engine.py',{mode:'text',args:engine_arguments});
    engine.on('message',(message)=>{
    console.log('engine python said : \n',message);  })
       
}
function turn(obj) 
{
    var engine_arguments = [obj.name,obj.sensitivity,obj.direction,obj.time]
    engine = new PythonShell(__dirname+'/robot/engine.py',{mode:'text',args:engine_arguments});
    engine.on('message',(message)=>{
    console.log('engine python said : \n',message);})
}

function stop(obj) { engine.kill();  }

function messge(obj) {  console.log('message received from user -> \n ',obj); }




