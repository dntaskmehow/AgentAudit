import argparse
from .ledger import AuditLedger, AuditEvent

def main():
    parser = argparse.ArgumentParser(description="AgentAudit Logger.")
    parser.add_argument("--agent", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--tokens", type=int, default=150)
    parser.add_argument("--status", default="SUCCESS")
    args = parser.parse_args()
    cost = args.tokens * 0.00002
    ledger = AuditLedger()
    event = AuditEvent(agent_id=args.agent, action=args.action, tokens_used=args.tokens, cost_usd=cost, status=args.status)
    ledger.record(event)
    print(f"[+] Audit event logged for agent '{args.agent}'.")

if __name__ == "__main__": main()
