const app = require('express')();
const express = require('express')
let http = require('http').createServer(app)
const io = require('socket.io')(http);
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



app.get('/', (req, res)=>{
    res.render('index', {
        data: textt
    })
})


port = 3030
http.listen(port, ()=>{
    console.log('http://goroscop.herokuapp.com/'+port)
})
//http.createS