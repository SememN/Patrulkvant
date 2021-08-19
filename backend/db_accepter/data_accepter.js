const {MongoClient} = require('mongodb');
const fs = require('fs');

async function main() {
    const uri = "mongodb+srv://Sam:2128506menemMENEM123@cluster0.7bhv1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

    const client = new MongoClient(uri);

    let db = client.db("patrul_coords");
    let coords = db.collection("coords");

    await client.connect();

    let find_results = await coords.find({ title: "coords" }).toArray();

    if (find_results.length) {
        let write = {
            coords: find_results[0].content
        };
        fs.writeFileSync("../routing/coords.json",JSON.stringify(write));
        coords.deleteOne({ title: "coords" });
        clearInterval(repeat);
        process.exit();
    }
}

let repeat = setInterval(main, 1000);
