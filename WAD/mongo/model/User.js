const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    name: {type:String, required:true},
    rollno: {type:Number,required:true},
    cc_mks: {type: Number},
    ai_mks: {type: Number},
    ds_mks: {type:Number},
    wad_mks: {type:Number}
})

module.exports = mongoose.model('User',userSchema);
// module is a variable that represents the current module and exports is an object that will be exposed as a module.
// Modules are self-contained units of functionality that can be shared and reused across projects. 
// In this case we have exposed the User model and from our app.js or from any other file in our project 
// we will be able to access it.
