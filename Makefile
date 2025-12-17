.PHONY: login logout whoami projects help

# Load environment variables from .env.local
include .env.local
export

help:
	@echo "Available commands:"
	@echo "  make login     - Log into OpenShift cluster"
	@echo "  make logout    - Log out from OpenShift cluster"
	@echo "  make whoami    - Show current user and cluster info"
	@echo "  make projects  - List all available projects"
	@echo "  make console   - Display console URL"

login:
	@echo "Logging into OpenShift cluster..."
	@oc login --server=$(OCP_SERVER) \
		--username=$(OCP_USERNAME) \
		--password='$(OCP_PASSWORD)' \
		--insecure-skip-tls-verify
	@echo "✓ Successfully logged in as $(OCP_USERNAME)"

logout:
	@echo "Logging out from OpenShift cluster..."
	@oc logout
	@echo "✓ Logged out"

whoami:
	@echo "Current user:"
	@oc whoami
	@echo ""
	@echo "Cluster version:"
	@oc version
	@echo ""
	@echo "Current project:"
	@oc project

projects:
	@echo "Available projects:"
	@oc projects

console:
	@echo "OpenShift Console URL:"
	@echo "$(OCP_CONSOLE)"

