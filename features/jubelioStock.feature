Feature: Jubelio Update Stock

  Scenario: Login to Jubelio with valid parameters
    Given Launch chrome browser
    When I am on the www.app.jubelio.com Login Page
    And Fill email field with "qa.rakamin.jubelio@gmail.com" and fill password with "Jubelio123!"
    And Click on Masuk button
    And Click on menu Barang and click on sub menu Persediaan
    And Click on Penyesuaian Persediaan button
    And Fill name product with "TWS 198" and fill stock product with "3"
    And Click on Simpan button
    Then User must successfully Update stock product

