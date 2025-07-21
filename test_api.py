#!/usr/bin/env python3
"""
Simple test script to verify the Flask task API functionality.
This tests basic CRUD operations and CSV export.
"""

import json
import requests
import time
import sys


def test_api():
    """Test the main API endpoints"""
    base_url = "http://127.0.0.1:5000"
    
    print("Testing Flask Task API...")
    print("-" * 40)
    
    try:
        # Test GET all tasks
        print("1. Testing GET /tareas")
        response = requests.get(f"{base_url}/tareas")
        if response.status_code == 200:
            tasks = response.json()
            print(f"✓ Success: Found {len(tasks['tareas'])} tasks")
        else:
            print(f"✗ Failed: Status {response.status_code}")
            return False
        
        # Test GET specific task
        print("\n2. Testing GET /tareas/1")
        response = requests.get(f"{base_url}/tareas/1")
        if response.status_code == 200:
            task = response.json()
            print(f"✓ Success: Task found - {task['tarea']['titulo']}")
        else:
            print(f"✗ Failed: Status {response.status_code}")
            return False
        
        # Test POST new task
        print("\n3. Testing POST /tareas")
        new_task = {
            "titulo": "Test Task from Script", 
            "descripcion": "This task was created by the test script"
        }
        response = requests.post(f"{base_url}/tareas", 
                               json=new_task,
                               headers={"Content-Type": "application/json"})
        if response.status_code == 201:
            created_task = response.json()
            task_id = created_task['tarea']['id']
            print(f"✓ Success: Created task with ID {task_id}")
        else:
            print(f"✗ Failed: Status {response.status_code}")
            return False
        
        # Test PUT update task
        print(f"\n4. Testing PUT /tareas/{task_id}")
        update_data = {"hecho": True}
        response = requests.put(f"{base_url}/tareas/{task_id}",
                              json=update_data,
                              headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            updated_task = response.json()
            print(f"✓ Success: Task marked as done - {updated_task['tarea']['hecho']}")
        else:
            print(f"✗ Failed: Status {response.status_code}")
            return False
        
        # Test CSV export
        print("\n5. Testing GET /tareas/export")
        response = requests.get(f"{base_url}/tareas/export")
        if response.status_code == 200 and response.headers.get('content-type') == 'text/csv; charset=utf-8':
            csv_lines = response.text.strip().split('\n')
            print(f"✓ Success: CSV export with {len(csv_lines)} lines (including header)")
        else:
            print(f"✗ Failed: Status {response.status_code} or wrong content type")
            return False
        
        # Test DELETE task
        print(f"\n6. Testing DELETE /tareas/{task_id}")
        response = requests.delete(f"{base_url}/tareas/{task_id}")
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Success: {result['resultado']}")
        else:
            print(f"✗ Failed: Status {response.status_code}")
            return False
        
        print("\n" + "=" * 40)
        print("✓ All tests passed successfully!")
        return True
        
    except requests.ConnectionError:
        print("✗ Error: Could not connect to Flask server.")
        print("Make sure the Flask app is running on http://127.0.0.1:5000")
        return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False


if __name__ == "__main__":
    if test_api():
        sys.exit(0)
    else:
        sys.exit(1)