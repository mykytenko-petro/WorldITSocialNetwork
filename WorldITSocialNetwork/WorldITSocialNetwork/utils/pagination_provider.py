from abc import ABC, abstractmethod
from typing import Any

from django.views.generic.base import View
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string


class PaginationProvider(View, ABC):
    @property
    @abstractmethod
    def queryset(self) -> Any:
        """
        Must return the queryset or list to be paginated.
        """
        pass

    @property
    @abstractmethod
    def template_name(self) -> str:
        """
        Must return template name.
        """
        pass

    @property
    def context(self) -> dict[str, Any]:
        """
        You can override it to include custom context.
        """
        return {}

    @property
    def per_page(self) -> int:
        """
        You can override it to include custom item count.
        """
        return 5

    def get(self, request: HttpRequest) -> HttpResponse:
        try:
            page = int(request.GET.get("page")) # type: ignore
        except (ValueError, TypeError):
            return HttpResponse("Invalid page or per_page parameters.", status=400)

        return self._get_pagination_response(page)

    def _get_pagination_response(self, page: int):
        paginator = Paginator(self.queryset, self.per_page)

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            return HttpResponse(status=204)

        return self.render(page_obj)
    
    def render(self, page_obj):
        '''
        You can override it to return custom response.
        '''
        html = render_to_string(
            self.template_name,
            {
                "page_obj": page_obj,
                **self.context
            }
        )

        return JsonResponse({
            "html": html
        })