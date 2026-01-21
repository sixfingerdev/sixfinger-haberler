#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script for Pexels thumbnail functionality
"""

import sys
sys.path.insert(0, '/home/runner/work/sixfinger-haberler/sixfinger-haberler')

from app import get_pexels_thumbnail, get_article_thumbnail

def test_pexels_integration():
    """Test Pexels API integration"""
    
    test_queries = [
        "Hasta hekim kendi şikayetlerine reflü tanısı koydu, hastalığı toplumda nadir görülen akalazya çıktı",
        "Suriye'deki DAEŞ'li mahkumlar Irak'a nakledilecek",
        "Teknoloji haberleri",
        "Ekonomi ve finans"
    ]
    
    print("=" * 80)
    print("🧪 Pexels Thumbnail Entegrasyonu Test Ediliyor...")
    print("=" * 80)
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{i}. Test Query: {query[:60]}...")
        
        # Test direct Pexels call
        result = get_pexels_thumbnail(query)
        if result:
            print(f"   ✅ Pexels URL: {result[:80]}...")
        else:
            print(f"   ❌ Pexels sonuç bulamadı")
        
        # Test with fallback
        fallback_result = get_article_thumbnail(query, "")
        if fallback_result:
            if "pexels" in fallback_result or "picsum" in fallback_result:
                print(f"   ✅ Fallback URL: {fallback_result[:80]}...")
            else:
                print(f"   ⚠️  Unexpected URL: {fallback_result[:80]}...")
        else:
            print(f"   ❌ Fallback başarısız")
        
        print("-" * 80)
    
    print("\n✅ Test tamamlandı!")

if __name__ == "__main__":
    test_pexels_integration()
