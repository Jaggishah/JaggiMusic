import mongoose from 'mongoose';

export const getSingleTrackController = async (req, res) => {
    try {
        let { page,limit } = req.query;
        page = page ?? 1 
        limit = limit ?? 16
        const collection = mongoose.connection.db.collection("single_track");

        const transcripts = await collection
                        .aggregate([
                            { $sort: { _id: -1 } }, // Sort by `_id`
                            { $skip: (page - 1) * limit }, // Pagination
                            { $limit: limit }, // Limit results
                            { 
                            $project: { 
                                _id: 0,       // Exclude `_id`
                                id: "$_id",   // Rename `_id` to `id`
                                title : 1,
                                artist : 1,
                                artwork : 1,
                                url : 1
                            } 
                            }
                        ])
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
