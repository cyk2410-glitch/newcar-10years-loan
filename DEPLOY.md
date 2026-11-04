# 아우디 홈페이지 배포 안내

1. 이 ZIP을 새 GitHub 저장소 `ag-audi-finance`에 압축 해제하여 업로드하세요. 기존 BMW/벤츠 프로젝트에 덮어쓰지 마세요.
2. Cloudflare Workers & Pages → Create → Pages → Connect to Git → 해당 저장소 선택. 프레임워크 None, 빌드 명령 비움, 출력 디렉터리 `/` 또는 `.`(화면 요구 형식에 맞게). `functions/` 폴더도 반드시 함께 배포하세요.
3. 실제 주소가 `https://<your-project>.pages.dev/`로 확정되면 `python prepare_domain.py https://<your-project>.pages.dev`를 실행하고 변경된 `index.html`, `robots.txt`, `sitemap.xml`을 GitHub에 반영하세요. 도메인을 임의로 가정하지 않았습니다.
4. 실제 주소의 `/api/latest-posts`를 열어 posts 6개(가능한 경우)와 warnings를 확인하세요. Naver RSS가 차단되거나 게시 지연 시 경고가 나옵니다.
5. 네이버 서치어드바이저와 Google Search Console에서 새 도메인 소유권 확인 → sitemap.xml 제출 → URL 검사. 검색 결과 노출은 보장되지 않습니다.
6. 기존 메인 Netlify 사이트는 삭제되었다고 하셨으므로 삭제된 링크를 넣지 않았습니다.

주의: 사례 4건의 사진은 정확한 차량 실물 사진이 확인되지 않아 차량별 텍스트 그래픽으로 표시했습니다. Q8 사례는 금액 상충으로 제외했습니다. Q5/A6 원고상 차량가도 원본 견적 확인이 필요합니다.

추가 검수: 모델 카드 18개 확정 반영. 확정 SEO 설명글 적용. 실제 배포 도메인 확정 전 canonical/OG 절대주소/사이트맵은 prepare_domain.py 실행 필요. 아우디 모델별 차량 사진은 현재 텍스트 카드로 제공되며, 사진 추가 제작은 별도 단계입니다.

## 2026-11-02 수정사항
- AG 원형 인물 파비콘: 루트 favicon.ico, 32/48/96 PNG 및 Apple 180 PNG 생성. 네이버·구글 검색 결과 표시 자체는 보장되지 않음.
- 아우디파이낸셜 비교 카드의 외부 아우디 공식 사이트 클릭 링크 제거. 정보 출처에 관한 설명은 유지, AG 맞춤 상담 버튼 추가.
- 실제 사례 제목을 AG 천팀장·120개월·10년 중심으로 변경, 900건 이상 타 차종 후기 연결 추가.
- SEO 원래 title/description, 18개 모델, 실제 사례 수치, 기존 RSS API 기능 유지.
- 모델별 실제 차량 이미지 제작·적용은 별도 단계이며 현재 텍스트 그래픽을 유지.

## 2026-11-03 SEO 이미지 보강
- 좌측 사이트 아이콘: 루트 favicon.ico 및 assets/favicon-32/48/96/192/512.png. 브라우저 미리보기는 파일 경로를 확인하세요.
- 우측 대표 이미지 후보: assets/brand.jpg. 본문 이미지도 유지. og:image, twitter:image, og:image:alt, twitter:card, max-image-preview:large 추가.
- **배포 전 필수:** 공개 Pages URL 확정 후 `python prepare_domain.py https://실제주소.pages.dev` 실행 → 변경된 index.html/robots.txt/sitemap.xml 업로드. 절대 URL은 배포 전에는 미확정입니다.
- 공개 배포 후 `/assets/brand.jpg`, `/favicon.ico`, `/api/latest-posts` 직접 열어 확인. 이미지 선택 및 노출은 검색엔진 재량입니다.
- 기존 실제 사례와 18개 모델 내용 유지. 자동차 실물 사진은 별도 작업입니다.


## v4.1 화면 검수 수정 (2026-11-03)
- 대표 사진 위 중복 바로가기 제거
- 실제 사례 섹션 제목·설명 가독성 개선
- 4개 사례 차종별 AI 생성 차량 참고 이미지 추가 (실제 고객 차량 촬영 사진이 아님)
- 중복 WHY AG CONSULTING 영역 삭제, brand.jpg를 AG 상담 경쟁력 섹션 메인 사진으로 이동
- 실제 사례 → 블로그 후기 → 상담 강점 순서 유지
- 실제 차량 사진이 확보되면 assets/audi-case-1~4.jpg를 교체하고 AI 생성 안내를 제거하세요.


## v4.3 변경사항
- 메인 좌측·우측 문구 수정: 월 할부 부담과 60/120개월 비교 질문 중심
- 실제 사례 4건 바로 아래에 120개월 할부 활용·총이자·차량 교체·부분상환 안내 섹션 추가
- 네비게이션 120개월 활용법 링크 및 FAQ 중도상환 질문 추가
- 실제 금융상품의 중도상환수수료, DSR, 대환·차량 매각 조건은 반드시 약정 확인
- 로컬 file://에서는 Cloudflare Pages Function(/api/latest-posts)이 실행되지 않습니다. 실제 배포 후 RSS 접근 및 최신 6건 표시 확인 필요
- 배포 전 prepare_domain.py를 공개 HTTPS 도메인으로 실행하여 OG/canonical/사이트맵 절대 URL 설정


v4.5: 금융상품 사진을 My브랜치 왼쪽 대형 / 오토론·EV 오른쪽 상하로 변경. 금융 선택 가이드 3장 클릭 확대/이전/다음 기능 복구. 실제 금융사 심사기준과 다른 참고용 인포그래픽이므로 반드시 최신 약관 확인.
