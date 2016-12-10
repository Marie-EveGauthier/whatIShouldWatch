<?php

namespace Tuto\TestBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class DefaultController extends Controller
{
    public function indexAction($name)
    {
        return $this->render('TutoTestBundle:Default:index.html.twig', array('name' => $name));
    }

    public function listeAction()
    {
        $film = $this->getDoctrine()
            ->getRepository('TutoTestBundle:Films')
        ->find();

        return $this->render('TutoTestBundle:Default:index.html.twig', array(
            'film' => $film->getTire(), 'realisator' => $film-> getRealisateur()
        ));

    }



}