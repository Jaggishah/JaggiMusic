import mongoose from 'mongoose';

export const getSingleTrackController = async (req, res) => {
    try {
        let { page,limit } = req.query;
        page = page ?? 1 
        limit = limit ?? 16
        const collection = mongoose.connection.db.collection("single_track");

        const transcripts = await collection
            .find({}, { projection: { _id: 0 } }) // Exclude the `id` field
            .sort({ _id: -1 }) // Sort by `id` in ascending order
            .skip((page - 1) * limit)
            .limit(limit)
            .toArray();

        res.status(200).json({
            message: "Data retrieved successfully",
            data: transcripts,
        });
    } catch (error) {
        console.error('Error fetching data:', error);
        res.status(500).json({
            message: "An error occurred while fetching data",
            error: error.message,
        });
    }
};
