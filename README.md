# Trend Sentinel

## 🚀 Project Overview

Trend Sentinel is a cutting-edge, real-time social media trend analysis and sentiment tracking platform. Designed for immediate insights, it captures, processes, and visualizes trending topics and public sentiment from a multitude of data sources. Leveraging a robust microservices architecture, the platform integrates powerful technologies like Kafka for high-throughput data streaming, TimescaleDB for efficient time-series data storage, Elasticsearch for rapid full-text search, and a dynamic Next.js frontend for an interactive and intuitive user experience.

The primary goal of Trend Sentinel is to empower users with an unparalleled understanding of the digital discourse, enabling swift comprehension of public perception, identification of emerging trends, and proactive response to critical discussions.

## ✨ Features

*   **Real-time Data Ingestion:** Utilizes Kafka as a central nervous system for consuming and routing high-volume data streams in real-time.
*   **Advanced Sentiment Analysis:** Employs sophisticated NLP models (like BERT) to perform granular sentiment analysis on incoming text data, categorizing it as positive, negative, or neutral.
*   **Dynamic Trending Topics:** Continuously monitors and identifies keywords, hashtags, and phrases that are gaining momentum across data sources.
*   **Powerful Search & Analytics:** Leverages Elasticsearch for lightning-fast full-text search, enabling users to delve into historical data with advanced querying capabilities.
*   **Optimized Time-Series Storage:** Stores and manages vast amounts of time-stamped data efficiently using TimescaleDB, perfect for trend analysis.
*   **Interactive Dashboard:** A modern, responsive Next.js frontend provides a comprehensive visual overview of live feeds, sentiment trends, trending topics, and viral alerts.
*   **Scalable & Resilient Architecture:** Built on a microservices paradigm with Docker Compose orchestration, ensuring high availability, fault tolerance, and easy horizontal scaling of individual components.
*   **Viral Alerting System:** Proactive notifications for topics that exhibit sudden and significant spikes in mentions, helping users stay ahead of the curve.

## 🏛️ System Architecture

Trend Sentinel is engineered with a scalable microservices architecture, designed for high performance and maintainability.