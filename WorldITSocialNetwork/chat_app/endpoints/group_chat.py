import string
import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import JsonResponse
from django.template.loader import render_to_string

from user_app.utils import get_all_friends


class ContactFilterView(LoginRequiredMixin, View):
    def get(self, _):
        return JsonResponse({"html": self.render_contacts()})

    def render_contacts(self):
        filtered_contacts = self.filter_contacts()
        raw_contacts = {}

        for letter, contacts in filtered_contacts.items():
            raw_contacts[letter] = render_to_string(
                "chat_app/particles/contact_card.html", {
                    "page_obj": contacts,
                    "mode": "select"
                }
            )

        rendered_contacts = [
            {'letter': letter, 'contact': contact} 
            for letter, contact in raw_contacts.items()
        ]

        return render_to_string(
            "chat_app/particles/filtered_contacts.html", {
            "rendered_contacts": rendered_contacts
        })

    def filter_contacts(self):
        contacts = get_all_friends(self.request.user)

        ukrainian_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        english_alphabet = string.ascii_uppercase

        filtered_contacts = {}
        
        for letter in ukrainian_alphabet:
            filtered_contacts[letter] = []
            
        for letter in english_alphabet:
            filtered_contacts[letter] = []
            
        filtered_contacts["#"] = []

        ukrainian_pattern = re.compile(r'^[А-ЩЬЮЯҐЄІЇа-щьюяґєії]')
        english_pattern = re.compile(r'^[A-Za-z]')

        for contact in contacts:
            name = contact.username

            first_char = name[0].upper() # type: ignore

            if ukrainian_pattern.match(first_char):
                filtered_contacts[first_char].append(contact)
            elif english_pattern.match(first_char):
                filtered_contacts[first_char].append(contact)
            else:
                filtered_contacts["#"].append(contact)

        cleaned_contacts = {k: v for k, v in filtered_contacts.items() if len(v) > 0}

        return cleaned_contacts