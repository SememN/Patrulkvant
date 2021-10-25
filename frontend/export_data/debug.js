const {MongoClient} = require('mongodb');

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