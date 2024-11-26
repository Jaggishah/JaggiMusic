import express from 'express';
import mongoose from 'mongoose';
import bodyParser from 'body-parser';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

import {connectDB} from "./CRUD/Connection.js"
import { getSingleTrackController } from "./Controllers/getSingleSongs.js"
// Initialize app
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(cors());

connectDB(process.env.CONNECTION_STRING)

// Basic Route
app.get('/', (req, res) => {
    res.send({"msg":"Hello World!"});
});

app.get('/single/',getSingleTrackController)
// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
