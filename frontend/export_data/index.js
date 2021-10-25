const hapi = require('hapi');
const {MongoClient} = require('mongodb');
const fs = require('fs');
let page = fs.readFileSync('map.txt').toString();
let terminal = fs.readFileSync('console.txt').toString();
let ficCode = fs.readFileSync('fiction_code.txt').toString();
let style = fs.readFileSync('style.txt').toString();
let mapStyle = fs.readFileSync('map.yaml').toString();
let Kvant = fs.readFileSync('kvantorium.png');
let DEBUG = false;

const server = hapi.server({
 port: 8000,
 host: 'localhost'
});

if (DEBUG) {
	async function debug () {
		const uri = "mongodb+srv://Alenigma:WhatAreYouDoingInMySwamp@patrulkvant.ramkj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
		
		let points = `{coords: { lat: 52.5309825, lng: 13.3845921 }, temp: 17.4, wet: 27, light: 25, p: 56},{coords: { lat: 52.5311923, lng: 13.3853495 }, temp: 17.4, wet: 27, light: 25, p: 56}`

		const client = new MongoClient(uri);

		let db = client.db("patrul_data");
		let coords = db.collection("weather");

		await client.connect();

		let weather_data = {
			title: "path",
			content: points
		}
		
		let result = await coords.insertOne(weather_data);
		console.log("YES")
	}
	debug()
}

let find_results

async function database () {
	const uri = "mongodb+srv://Alenigma:WhatAreYouDoingInMySwamp@patrulkvant.ramkj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
	let change = "let points = ["
	let changeStyle = "<style>"
	let insertFictionCode = "let blah = `"
		
	const client = new MongoClient(uri);

	let db = client.db("patrul_data");
	let path = db.collection("weather");

	await client.connect();

	find_results = await path.find({ title: "path" }).toArray();
	if (find_results.length) {
		let points = find_results[0].content
		
		path.deleteOne({ title: "path" });
		
		let a = page.split('');
		let find = page.indexOf(change) + change.length
		let findStyle = page.indexOf(changeStyle) + changeStyle.length
		a.splice(find, 0, points);
		a.splice(findStyle, 0, style);
		page = a.join('')
	}
	
	let b = terminal.split('');
	
	let findInsert = terminal.indexOf(insertFictionCode) + insertFictionCode.length
	
	b.splice(findInsert, 0, ficCode);
	
	terminal = b.join('')
}

	const init = async () => {
		server.route([{
			method: 'GET',
			path: '/',
			handler: async function (request, reply) {
				await database();
				if (find_results.length) {
					return `<script> async function redir () {await sleep(100); window.location = "/final"}; redir(); function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms));} </script>`
				} else {
					return `<script> async function redir () {await sleep(100); window.location = "/terminal"}; redir(); function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms));} </script>`
				}
				
				//Спрсить по точности маршрута
			}
		},
		{
		method: 'GET',
			path: '/map.yaml',
			handler: async function (request, reply) {
				return mapStyle;
			}
		},
		{
		method: 'GET',
			path: '/final',
			handler: async function (request, reply) {
				await database();
				return page;
			}
		},
		{
		method: 'GET',
			path: '/terminal',
			handler: async function (request, reply) {
				return terminal;
			}
		},
		{
		method: 'GET',
			path: '/kvantorium',
			handler: async function (request, reply) {
				return Kvant;
			}
		}]);
		await server.start();
		console.log(`Server running at: ${server.info.uri}`);
	};
	init();
database();