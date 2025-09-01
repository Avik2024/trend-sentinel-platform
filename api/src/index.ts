
import express from "express";
import trendingRouter from "./routes/trending";
import sentimentRouter from "./routes/sentiment";
import searchRouter from "./routes/search";

const app = express();
app.use(express.json());

app.use("/trending", trendingRouter);
app.use("/sentiment", sentimentRouter);
app.use("/search", searchRouter);

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => console.log(`API running on port ${PORT}`));
