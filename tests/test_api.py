

def test_listing_club_api(client):
    resp = client.get('/clubs/')
    assert resp.status_code == 200
    assert len(resp.json()) == 411


def test_query_club_api(client):
    resp = client.get('/clubs/query/', params={
        'query': "what club have the highest stadium seats"
    })
    resp_data = resp.json()
    assert resp.status_code == 200
    assert 'FC Barcelona' in resp_data['response_text']
    assert '99,354' in resp_data['response_text']
