

// создаем объект MongoClient и передаем ему строку подключения
const MongoClient = require('mongodb').MongoClient;
const uri = 'mongodb+srv://limerencia:lim@cluster0-2ykfb.mongodb.net/test?retryWrites=true&w=majority';
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, });
client.connect(async (err) => {
        
    const db = client.db("test");
    const collection = db.collection("user");
    let user = {name: "Tom", age: 23};
    await collection.insertOne({sSdSd:"sadsdsd"}, function(err, result){
      
        if(err){ 
            return console.log(err);
        }
        console.log(result);
        client.close();
    });
});
