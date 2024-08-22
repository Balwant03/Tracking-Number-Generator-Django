from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
import hashlib
import datetime

def generate_uuid_from_customer_id(customer_id):
    # Create a SHA-1 hash of the customer_id
    hash_object = hashlib.sha1(customer_id.encode())
    # Take the first 16 bytes of the hash and convert it to a UUID
    hash_bytes = hash_object.digest()[:16]
    # Create a UUID from the hash bytes
    return str(uuid.UUID(bytes=hash_bytes))


class NextTrackingNumberView(APIView):
    def get(self, request):
        # Extract query parameters
        origin_country_id = request.query_params.get('origin_country_id')
        destination_country_id = request.query_params.get('destination_country_id')
        weight = request.query_params.get('weight')
        customer_id = request.query_params.get('customer_id')
        customer_name = request.query_params.get('customer_name')
        customer_slug = request.query_params.get('customer_slug')

        # Validation
        if not all([origin_country_id, destination_country_id, weight,customer_id, customer_name, customer_slug]):
            return Response({"error": "Missing required query parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Validate and parse parameters
            weight = float(weight)
            created_at = datetime.datetime.now().isoformat()
            uuid_customer_id = generate_uuid_from_customer_id(customer_id)
            uuid.UUID(uuid_customer_id)  # Validate UUID
        except (ValueError, TypeError):
            return Response({"error": "Invalid parameter format"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate tracking number (example logic)
        tracking_number = str(uuid.uuid4().hex[:12])

        # Respond with the tracking number
        return Response({"tracking_number": tracking_number, "created_at": created_at})
