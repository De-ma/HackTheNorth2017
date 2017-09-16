//
//  ViewController.swift
//  myRoomMate
//
//  Created by Dema Abu Adas on 2017-09-16.
//  Copyright © 2017 Dema Abu Adas. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var doorView: UIView!
    @IBOutlet weak var view1: UIView!
    @IBOutlet weak var lightView: UIView!
    
    var tapGesture1 = UITapGestureRecognizer()
    var tapGestureDoor = UITapGestureRecognizer()
    var tapGestureLight = UITapGestureRecognizer()
    
    @IBOutlet weak var lightPhotoView: UIImageView!


    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.lightPhotoView.backgroundColor = UIColor(patternImage: UIImage(named: "light.png")!)
        
        tapGesture1 = UITapGestureRecognizer(target: self, action: #selector(ViewController.myviewTapped1(_:)))
        tapGesture1.numberOfTapsRequired = 1
        tapGesture1.numberOfTouchesRequired = 1
        view1.addGestureRecognizer(tapGesture1)
        view1.isUserInteractionEnabled = true
        
        tapGestureDoor = UITapGestureRecognizer(target: self, action: #selector(ViewController.myviewTappedDoor(_:)))
        tapGestureDoor.numberOfTapsRequired = 1
        tapGestureDoor.numberOfTouchesRequired = 1
        doorView.addGestureRecognizer(tapGestureDoor)
        doorView.isUserInteractionEnabled = true
        
        tapGestureLight = UITapGestureRecognizer(target: self, action: #selector(ViewController.myviewTappedLight(_:)))
        tapGestureLight.numberOfTapsRequired = 1
        tapGestureLight.numberOfTouchesRequired = 1
        lightView.addGestureRecognizer(tapGestureLight)
        lightView.isUserInteractionEnabled = true
    }
    
    func myviewTapped1(_ sender: UITapGestureRecognizer) {
        //What happens when view1 is tapped!
        if self.view1.backgroundColor == UIColor.yellow {
            self.view1.backgroundColor = UIColor.black
        } else {
            self.view1.backgroundColor = UIColor.yellow
        }
    }
    
    func myviewTappedDoor(_ sender: UITapGestureRecognizer) {
        //What happens when doorview is tapped!
        if self.doorView.backgroundColor == UIColor.green {
            self.doorView.backgroundColor = UIColor.purple
        } else {
            self.doorView.backgroundColor = UIColor.green
        }
    }
    
    func myviewTappedLight(_ sender: UITapGestureRecognizer) {
        //What happens when lightview is tapped!

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

