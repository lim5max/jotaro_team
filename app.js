require('dotenv').config()
const app = require('express')();
const express = require('express');

let http = require('http').createServer(app)
const { DateTime } = require("luxon");
const fs = require('fs')
let session = require('express-session')
const fs1 = require('promise-fs')
const helmet = require('helmet');
const io = require('socket.io')(http);
const bodyParser = require('body-parser')
const { body, validationResult } = require('express-validator');
const router = new express.Router();
textt = [
    "✨ Завтра окружающие будут атаковать вас вопросами и предложениями. Вы сможете отлично провести время с друзьями и при этом завести новые знакомства. Благодаря вашей обаятельности вы без труда вызываете у людей доверие.",
    "✨ В этот день вы можете проявить некоторую эксцентричность, что не самым приятным образом отразится на вашей деятельности. Не идите на поводу у чужого мнения. Вам следует больше доверять собственной интуиции, поскольку именно она сможет в нужный момент подсказать правильное решение в той или иной ситуации.",
    "✨ Завтра вы будете окружены доброжелателями. Это суровое испытание, но если вам удастся его выдержать и от них не сбежать, вы будете щедро вознаграждены за мужество."
]

app.engine('ejs', require('ejs-locals'));
app.set('views', __dirname+'/templates/' );
app.set('view engine', 'ejs');
app.use(bodyParser.json());
app.use(session({ secret: 'keyboard cat', cookie: { maxAge: 60000 }}))

app.use(bodyParser.urlencoded({ extended: true }));
app.use(helmet());



app.get('/', (req, res)=>{
    res.render('horoscope1', {
        data: {
            error: []
        }
    })
})
app.post("/", async (req, res)=>{

    
    let error = {error: []}

    let name = req.body.username
    let date = req.body.newdate
    //console.log(date)
    let now = DateTime.local();
    let user_date = DateTime.fromISO(date)
    let age = now.year - user_date.year
    let password = req.body.password
    if (password.length < 5 ){
        error.error.push("Длина пароля не менее 5 символов")
    }
    if (name.length < 6){
        error.error.push("Имя пользователя должно быть не менее 5 символов")
    }
    let user= {}
    if (error.error.length == 0){
        user = {
            password : password,
            name: name,
            interests: Math.round(Math.random(1, 16)),
            date: date,
            age : age,
            key_words : []

        }
    req.session.user = {
        username : user.name,
        password : user.password,
        age: user.age,
        interests: user.interests
    }
        console.log(user)
        async function GET_JSON (){


            
            daat = 0
            await fs1.readFile(__dirname+"/json/user.json").then(data=>{
                daat = JSON.parse(data)
            })
            return daat

        }
        data = await GET_JSON()
        console.log(data)
        
        
        data.push((user))
        fs.writeFileSync(__dirname+"/json/user.json", JSON.stringify(data))
        res.redirect('/login')
    }else{
        console.log(error)
        res.render('horoscope1', {
            data : error
        })
    }
    
})

app.get('/login', (req, res)=>{
    res.render('login')
    
    
})
app.get('/main', (req, res)=>{
    if (req.session.user){
        var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
    var process = spawn('python',[__dirname+"./rand5.py", 
                            req.session.name, 
                            req.session.age,
                            req.session.interests
                        ] ); 
  
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object 
    process.stdout.on('data', function(data) { 
        console.log(data.toString()) 
    } ) 
        res.render('main')
    }else{
        res.redirect('/login')
    }
    
})
app.post('/login', async (req, res)=>{
    let password = req.body.password
    let username = req.body.username
    console.log(password)
    async function GET_JSON (){


            
        daat = 0
        await fs1.readFile(__dirname+"/json/user.json").then(data=>{
            daat = JSON.parse(data)
        })
        return daat

    }
    daat = await GET_JSON()
 

        daat.forEach(element => {
        

            if( element.password.toLowerCase() == password.toLowerCase() && element.name.toLowerCase() == username.toLowerCase()){
                console.log(1)
                req.session.user = {
                    username : element.name,
                    password : element.password,
                    age : element.age,
                    interests: element.interests

                }
                console.log(req.session.user)
                res.redirect('/main')
            }
        })
   
 
    

    
})
port = process.env.PORT || 8080
http.listen(port, ()=>{
    console.log('http://gorosc.herokuapp.com/'+port)
})
//http.createS