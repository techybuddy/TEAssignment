const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const app = express();
const router = express.Router();
const User = require("./model/User");
const { db } = require('./model/User');

app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());
app.set("view engine", "ejs");


//const URL = "mongodb+srv://kardilechaitanya:fdsaghjk@cluster0.5dbkv.mongodb.net/studentDB?retryWrites=true&w=majority"
const URL = "mongodb://127.0.0.1:27017/studentDB"
mongoose.connect(URL, function(){
    console.log("Connected to mongodb successfully.");
});

app.listen(3000,function(){
    console.log("Server listening on port 3000");
});


// code for creating documents inside users collection
//var MongoClient = require('mongodb').MongoClient;

/*
MongoClient.connect("mongodb://127.0.0.1:27017/", function(err, db) {
  if (err) throw err;
  var dbo = db.db("studentDB");
  var myobj = [
    { name: 'John', rollno:81, cc_mks:99, ai_mks:88 , ds_mks: 89, wad_mks: 95},
    { name: 'Chaitanya', rollno:62, cc_mks:99, ai_mks:68 , ds_mks: 80, wad_mks: 75},
    { name: 'Shyam', rollno:12, cc_mks:89, ai_mks:98 , ds_mks: 87, wad_mks: 85}
  ];
  dbo.collection("users").insertMany(myobj, function(err, res) {
    if (err) throw err;
    console.log("Number of documents inserted: " + res.insertedCount);
    db.close();
  });
});
*/
module.exports = router;



 

app.get("/", function (req, res) {
    res.send("Mock practice")
})

app.get("/getdetails", function (req, res) {   
    User.find({}, function (err, allDetails) {
        if (err) {
            console.log(err);
        } else {
            res.render("index", { details: allDetails })
        }
    })
})

// app.get("/",function(req,res){
//  res.render("gte",{ details: null })
// })
app.get("/gte", function (req, res) {   

    User.find({ds_mks:{$gte:85}}, function (err, allDetails) {
        if (err) {
            console.log(err);
        } else {
            res.render("index", { details: allDetails })
        }
    })
})


app.get("/update" , function(req , res){
    var myquery = { rollno: 62 };
    var newvalues = { $inc: {cc_mks: 10, ds_mks: 10,ai_mks: 10,wad_mks: 10} };
    User.updateOne(myquery, newvalues, function(err, allDetails) {
        if (err) 
            console.log(err);
        console.log("1 document updated");
        // res.render("index", { details: allDetails })
        res.send("one document updated")
    });
})


app.get("/delete" , function(req , res){
    var myquery = { rollno: 62 };
    User.deleteOne(myquery, function(err, allDetails) {
        if (err) 
            console.log(err);
        console.log("1 document deleted");
        // res.render("index", { details: allDetails })
        res.send("one document deleted")
    });
})
 
