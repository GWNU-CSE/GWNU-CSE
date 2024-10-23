# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import UserProfile
import json

@csrf_exempt  # CSRF 토큰 검사를 비활성화 (테스트용, 실제로는 인증 적용 필요)
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 클라이언트에서 전송된 JSON 데이터 파싱
            email = data.get('email')
            password = data.get('password')
            nickname = data.get('nickname')

            # 새로운 사용자 생성 및 데이터베이스 저장
            user = UserProfile.objects.create(email_id=email, password=password, nickname=nickname)
            return JsonResponse({'message': 'User registered successfully', 'user_id': user.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def save_qr_url(request, user_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 클라이언트에서 전송된 JSON 데이터 파싱
            url = data.get('url')

            # URL 유효성 검사
            validator = URLValidator()
            try:
                validator(url)
            except ValidationError:
                return JsonResponse({'error': 'Invalid URL'}, status=400)

            # 해당 사용자 찾기
            user = UserProfile.objects.get(id=user_id)
            user.urls.append(url)  # URL 리스트에 새로운 URL 추가
            user.save()

            return JsonResponse({'message': 'URL saved successfully', 'user_id': user.id}, status=201)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
