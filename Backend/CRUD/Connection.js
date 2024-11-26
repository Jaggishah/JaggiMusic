import mongoose from "mongoose";

export const connectDB = async (URL) => {
  try {
    const conn = await mongoose.connect(URL);

    console.log(`MongoDB connected: ${conn.connection.host}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1); // Exit the process if connection fails
  }
};

