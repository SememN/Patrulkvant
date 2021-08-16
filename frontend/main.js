const hapi = require('hapi');
const {MongoClient} = require('mongodb');
const fs = require('fs');
const page = fs.readFileSync('html.txt').toString();

const server = hapi.server({
	port: 4000,
	host: 'localhost'
});

const init = async () => {
	server.route([
		{
			method: 'GET',
			path: '/',
			handler: function (request, reply) {
				return page;
			}
		}]);
	await server.start();
	console.log(`Server running at: ${server.info.uri}`);
};
init();

server.route([{
  method: 'POST',
  path: '/',
  config: {
      payload: {
          output: 'data'
      }
  },
  handler: function (request, response){
    let most = request.payload.most
	const uri = "mongodb+srv://Sam:2128506menemMENEM123@cluster0.7bhv1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
	async function main (most) {
		const client = new MongoClient(uri);
		let db = client.db("patrul_coords");
		let coords = db.collection("coords");
		await client.connect();
		let coords_data = {
			title: "coords",
			content: most
		}
		let result = await coords.insertOne(coords_data);
	}
	main(most);
  }
}]);