require('dotenv').config()
const app = require('express')();
const express = require('express')
let http = require('http').createServer(app)
const { DateTime } = require("luxon");
const fs = require('fs')

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

app.use(bodyParser.urlencoded({ extended: true }));


app.get('/', (req, res)=>{
    res.render('horoscope', {
        data: {
            error: []
        }
    })
})
app.post("/", (req, res)=>{

    
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
        console.log(user)
        fs.writeFileSync(__dirname+"/json/user.json", user)
    }else{
        console.log(error)
        res.render('horoscope', {
            data : error
        })
    }
    
})


port = process.env.PORT || 8080
http.listen(port, ()=>{
    console.log('http://gorosc.herokuapp.com/'+port)
})
//http.createS