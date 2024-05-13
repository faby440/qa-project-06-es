import sender_stand_request
import data
import configuration

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_client_kit(name)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()

    str_user = kit_body["name"] + "," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1
def negative_assert_code_400(kit_body):
    kit_body = get_kit_body("name")
    response = sender_stand_request.post_new_client_kit("name")
    assert response.status_code == 400

    assert response.json()["code"] == 400

    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400

    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

def test_kit_body_1_letter_in_name_get_success_response():
    positive_assert: ("a")
#2
def test_kit_body_511_letter_in_name_get_success_response():
    positive_assert: { "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
#3
def test_kit_body_0_letter_in_name_get_error_response():
    negative_assert_code_400: { "name": "" }
#4
def test_kit_body_512_letter_in_name_get_error_response():
    negative_assert_code_400: { "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
#5
def test_kit_body_has_special_symbol_in_name_get_success_response():
    positive_assert: {"name": "\"№%@\"," }
#6
def test_kit_body_has_space_in_name_get_success_response():
    positive_assert: { "name": " A Aaa " }
#7
def test_kit_body_has_number_in_name_get_success_response():
    positive_assert:("123")
#8
def test_create_kit_body_empty_name_get_error_response():
    negative_assert_no_name:{}
def test_create_kit_body_number_type_name_get_error_response():
    negative_assert_code_400: (12)
    response = sender_stand_request.post_new_user("kit_body")

    assert response.status_code == 400