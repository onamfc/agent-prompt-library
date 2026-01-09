# Cost & Performance Forecaster

An AI agent that estimates infrastructure costs and performance characteristics before systems are built, enabling informed architectural decisions.

## When to Use

- Evaluating architectural options and comparing cost/performance trade-offs
- Planning for scale and forecasting system behavior as traffic or data grows
- Pre-migration analysis to estimate costs before changing platforms or services
- Infrastructure design to identify potential bottlenecks and cost drivers early
- Budget planning to get rough order-of-magnitude cost estimates
- Technology selection to compare alternatives (databases, cloud providers, messaging systems)

## When NOT to Use

- Exact pricing quotes (this agent provides estimates and ranges, not billing predictions)
- Post-implementation optimization (use performance profiling tools and actual metrics instead)
- Simple, well-understood patterns (if you're building a standard CRUD app, forecasting may be overkill)
- Greenfield experiments (when validating ideas, build first and optimize later)

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|------------|-------|
| Claude Code | Excellent  | Best for interactive analysis with code context |
| Cursor      | Good       | Good for inline architecture discussions |
| Claude API  | Excellent  | Use Sonnet 4.5 or Opus 4.5; Opus for complex multi-system comparisons |

## Context Requirements

This agent works best with:

- Architecture diagrams or descriptions (components, data flows, dependencies)
- Scale assumptions (expected traffic, data volume, growth rate)
- Technology stack details (cloud provider, services, databases, frameworks)
- Performance requirements (latency targets, throughput needs, availability goals)
- Current costs (if applicable, for comparison or optimization scenarios)

## Example Prompts

```
"We're choosing between PostgreSQL on RDS and DynamoDB for a user profile service.
Expected: 100k users, 50 reads/writes per user/day, 2KB avg document size.
Compare cost and performance characteristics."

"Our API currently handles 1k req/s. We expect 10x growth over 6 months.
Current stack: Node.js on EC2 t3.medium, Redis cache, RDS PostgreSQL.
Where will we hit bottlenecks? What will cost increase look like?"

"Considering moving from monolith on EC2 to Lambda + API Gateway + DynamoDB.
Current: 500k daily active users, 10M requests/day, 200ms p95 latency.
Forecast cost and performance implications of serverless migration."

"Need to choose a message queue for background jobs: SQS, RabbitMQ on EC2, or Redis.
Volume: 10k jobs/hour, avg 5KB payload, jobs must be processed within 5 minutes.
Compare cost, reliability, and operational complexity."

"We're adding real-time features to our app. Compare WebSockets vs Server-Sent Events vs polling.
Expected: 50k concurrent connections, 10 messages/min per user."

"Estimate the cost difference between storing 5TB of user-generated images in S3 Standard vs S3 Intelligent-Tiering.
Access pattern: 80% of requests are for images uploaded in the last 30 days."
```

## Limitations

- Provides estimates and ranges, not exact billing predictions
- Forecasts are only as accurate as the assumptions provided
- Does not have access to real-time cloud pricing (pricing changes frequently)
- Cannot profile actual code performance (analysis is architectural, not algorithmic)
- Requires specific scale assumptions to provide meaningful estimates

## Customization

Fork and modify for:

- Industry-specific cost models (fintech compliance costs, healthcare data retention)
- Custom pricing databases for internal services or private cloud
- Team-specific risk tolerance and optimization preferences
- Organization-specific architectural patterns and standards
