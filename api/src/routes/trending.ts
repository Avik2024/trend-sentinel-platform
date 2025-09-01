import { Router } from "express";
const router = Router();

router.get("/", (req, res) => {
  res.json({ trending: ["trend1", "trend2"] });
});

export default router;
