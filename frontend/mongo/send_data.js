const {MongoClient} = require('mongodb');

async function main() {
    const uri = "mongodb+srv://Sam:2128506menemMENEM123@cluster0.7bhv1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

    const client = new MongoClient(uri);

    const db = client.db('patrul_coords');
    const coords = db.collection("coords");

    try {
        await client.connect();

        const doc = {
                        title: "Record of a Shriveled Datum",
                        content: "No bytes, no problem. Just insert a document, in MongoDB",
                    }

        const result = await coords.insertOne(doc);
        console.log(`A document was inserted with the _id: ${result.insertedId}`);
    }

    finally {
        await client.close();
    }

}

while (True){
    if (cainPoints == 7){
        main().catch(console.dir);
    }
}