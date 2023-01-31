import os
import allure
import pytest

@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('在fixture前置操作里面添加一个附件txt', 'fixture前置附件', allure.attachment_type.TEXT)

    def finalizer_module_scope_fixture():
        allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件',allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)


def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    pass


def test_multiple_attachments():
    allure.attach('<head></head><body>html page</body>', 'Attach with HTML type', allure.attachment_type.HTML)
    allure.attach.file('/Users/mrjade/Downloads/happy-new-year.html', attachment_type=allure.attachment_type.HTML)


pytest.main(['-s', '-q', 'attach_demo.py', '--clean-alluredir', '--alluredir=result'])
os.system(r"allure serve result")